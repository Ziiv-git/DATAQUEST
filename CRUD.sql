# /home/dq$ sqlite3 chinook.db
#
#  sqlite3> .tables
#  sqlite3> .headers on
#  sqlite3> .mode column
#  sqlite3> SELECT
#      ...>   track_id,
#      ...>   name,
#      ...>   album_id
#      ...> FROM track
#      ...> WHERE album_id = 3;
#  sqlite3> .help
#  sqlite3> .shell clear
#  sqlite3> .quit

# /home/dq$ sqlite3 new_database.db
#  sqlite3> CREATE TABLE user (
#      ...> user_id INTEGER,
#      ...> first_name TEXT,
#      ...> last_name TEXT
#      ...> );
#  sqlite3> .schema user
#  sqlite3> .quit

#  sqlite3> CREATE TABLE wishlist (
#      ...> wishlist_id INTEGER PRIMARY KEY,
#      ...> customer_id INTEGER,
#      ...> name TEXT,
#      ...> FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
#      ...> );
#  sqlite3> .quit
#

CREATE TABLE wishlist_track (wishlist_id INTEGER, track_id INTEGER, PRIMARY KEY (wishlist_id, track_id), FOREIGN KEY (wishlist_id) REFERENCES
wishlist(wishlist_id), FOREIGN KEY (track_id) REFERENCES track(track_id));


# /home/dq$ sqlite3 chinook.db
#  sqlite3> INSERT INTO wishlist
#      ...> VALUES
#      ...>     (1, 34, "Joao's awesome wishlist"),
#      ...>     (2, 18, "Amy loves pop");
#  sqlite3> INSERT INTO wishlist_track
#      ...> VALUES
#      ...>     (1, 1158),
#      ...>     (1, 2646),
#      ...>     (1, 1990),
#      ...>     (2, 3272),
#      ...>     (2, 3470);
#  sqlite3> .quit
#

sqlite3 chinook.db <<EOF
ALTER TABLE wishlist
ADD COLUMN active NUMERIC;
ALTER TABLE wishlist_track
ADD COLUMN active NUMERIC;
EOF



sqlite3 chinook.db <<EOF
ALTER TABLE invoice
ADD COLUMN tax NUMERIC;
ALTER TABLE invoice
ADD COLUMN subtotal NUMERIC;
UPDATE invoice
SET
    tax = 0,
    subtotal = total;
EOF
