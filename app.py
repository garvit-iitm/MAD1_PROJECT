from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime
from models.database import db, User, Admin, ParkingLot, ParkingSpot, Reservation

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parking_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'garvit123'

db.init_app(app)

def create_database():
    with app.app_context():
        db.create_all()
        print("Database and tables created successfully!")

@app.route("/login", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash('Please fill out both fields.', 'warning')
            return redirect(url_for('login_page'))

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            session['username'] = username
            flash(f'Login successful! Welcome to the User Dashboard, {username}!', 'success')
            return redirect(url_for('user_page'))
        elif username == 'admin' and password == 'admin123':
            session['username'] = username
            return redirect(url_for('admin_page'))
        else:
            flash('Invalid username or password.', 'danger')
            return redirect(url_for('login_page'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('login_page'))
    return render_template('register.html')

@app.route("/user")
def user_page():
    if 'username' in session:
        username = session['username']
        return render_template('user.html', username=username)
    flash("Please login first.", "warning")
    return redirect(url_for('login_page'))

@app.route("/admin")
def admin_page():
    username = session.get('username')
    lots = ParkingLot.query.all()
    for lot in lots:
        lot.occupied_spots = ParkingSpot.query.filter_by(lot_id=lot.id, status='O').count()
    return render_template('admin.html', lots=lots)

@app.route('/admin/admin_parkinglots')
def admin_parkinglots():
    lots = ParkingLot.query.all()
    for lot in lots:
        lot.occupied_spots = ParkingSpot.query.filter_by(lot_id=lot.id, status='O').count()
    return render_template('admin_parkinglots.html', lots=lots)

@app.route('/admin/add_lot', methods=['GET', 'POST'])
def add_parking_lot():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        address = request.form['address']
        pin_code = request.form['pin']
        max_spots = int(request.form['max_spots'])
        lot = ParkingLot(prime_location_name=name, price=price, address=address, pin_code=pin_code, maximum_number_of_spots=max_spots)
        db.session.add(lot)
        db.session.flush()
        for i in range(1, max_spots + 1):
            spot = ParkingSpot(lot_id=lot.id, status='A', spot_number=f"Spot-{i}")
            db.session.add(spot)
        db.session.commit()
        flash("Parking Lot Added with Spots!", "success")
        return redirect(url_for('admin_parkinglots'))
    return render_template('add_lot.html')

@app.route('/admin/deletelot/<int:lot_id>')
def delete_parking_lot(lot_id):
    lot = ParkingLot.query.get_or_404(lot_id)
    ParkingSpot.query.filter_by(lot_id=lot.id).delete()
    db.session.delete(lot)
    db.session.commit()
    flash("Parking Lot and its Spots Deleted!", "danger")
    return redirect(url_for('admin_parkinglots'))

@app.route('/admin/lot_details/<int:lot_id>')
def lot_details(lot_id):
    lot = ParkingLot.query.get_or_404(lot_id)
    spots = ParkingSpot.query.filter_by(lot_id=lot_id).all()
    return render_template('lot_details.html', lot=lot, spots=spots)

@app.route('/admin/admin_users')
def admin_users():
    users = User.query.all()
    return render_template('admin_users.html', users=users)

@app.route('/admin/spot_details/<int:spot_id>')
def spot_details(spot_id):
    spot = ParkingSpot.query.get_or_404(spot_id)
    return render_template('spot_details.html', spot=spot)

@app.route('/admin/delete_spot/<int:spot_id>', methods=['POST'])
def delete_spot(spot_id):
    spot = ParkingSpot.query.get_or_404(spot_id)
    lot = ParkingLot.query.get(spot.lot_id)
    if spot.status == 'A':
        db.session.delete(spot)
        db.session.commit()
        occupied_count = ParkingSpot.query.filter_by(lot_id=lot.id, status='O').count()
        lot.occupied_spots = occupied_count
        db.session.commit()
        flash("Spot Deleted!", "success")
    else:
        flash("Cannot delete an Occupied Spot!", "danger")
    return redirect(url_for('lot_details', lot_id=spot.lot_id))

@app.route('/admin/occupied_spot_details/<int:spot_id>')
def occupied_spot_details(spot_id):
    spot = ParkingSpot.query.get_or_404(spot_id)
    reservation = Reservation.query.filter_by(spot_id=spot.id).first()
    return render_template('occupied_spot_details.html', spot=spot, reservation=reservation)

@app.route('/search', methods=['GET'])
def search():
    filter_by = request.args.get('filter_by')
    query = request.args.get('query')
    lots = []

    if filter_by == 'user_id':
        user = User.query.filter_by(id=query).first()
        if user:
            reservations = Reservation.query.filter_by(user_id=user.id).all()
            lot_ids = list(set([res.lot_id for res in reservations]))
            lots = ParkingLot.query.filter(ParkingLot.id.in_(lot_ids)).all()
    elif filter_by == 'location':
        lots = ParkingLot.query.filter(ParkingLot.prime_location_name.ilike(f'%{query}%')).all()

    for lot in lots:
        lot.occupied_spots = ParkingSpot.query.filter_by(lot_id=lot.id, status='O').count()
        lot.spots = ParkingSpot.query.filter_by(lot_id=lot.id).all()

    return render_template('search.html', lots=lots)

@app.route('/admin/editlot/<int:lot_id>', methods=['GET', 'POST'])
def editlot(lot_id):
    lot = ParkingLot.query.get_or_404(lot_id)
    if request.method == 'POST':
        lot.prime_location_name = request.form['prime_location_name']  # use correct key
        lot.address = request.form['address']  # make sure this matches HTML
        lot.pin_code = request.form['pin_code']  # ensure this too
        lot.maximum_number_of_spots = int(request.form['maximum_number_of_spots'])
        db.session.commit()
        flash('Parking Lot updated successfully!', 'success')
        return redirect(url_for('admin_parkinglots'))
    return render_template('editlot.html', lot=lot)


@app.route('/admin/summary')
def summary():
    lots = ParkingLot.query.all()
    lot_names = [lot.prime_location_name for lot in lots]
    revenues = [lot.price * ParkingSpot.query.filter_by(lot_id=lot.id, status='O').count() for lot in lots]

    total_available = ParkingSpot.query.filter_by(status='A').count()
    total_occupied = ParkingSpot.query.filter_by(status='O').count()

    return render_template('summary.html', 
                           lot_names=lot_names, 
                           revenues=revenues, 
                           total_available=total_available, 
                           total_occupied=total_occupied)



if __name__ == "__main__":
    create_database()
    app.run(debug=True, port=5054)