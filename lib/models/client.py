# lib/models/client.py
from models.__init__ import CURSOR, CONN
from models.stylist import Stylist   

class Client:

  all = {}
  def __init__(self, name, phone_number, email, stylist_id, id=None):
    self.id = id
    self.name = name
    self.phone_number = phone_number
    self.email = email
    self.stylist_id = stylist_id

  def __repr__(self):
   return f"ID: {self.id} - {self.name}, {self.phone_number}, {self.email}, Stylist ID: {self.stylist_id}" 
  
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    if isinstance(name, str) and len(name):
      self._name = name
    else:
      raise ValueError("Name must be a non-empty string.")
    
  @property
  def phone_number(self):
    return self._phone_number
  
  @phone_number.setter
  def phone_number(self, phone_number):
    if len(phone_number) == 10 and int(phone_number):
      self._phone_number = phone_number
    else:
      raise ValueError("Phone number must be 10 digits.")
    
  @property
  def email(self):
    return self._email
  
  @email.setter
  def email(self, email):
    if isinstance(email, str) and len(email):
      self._email = email
    else:
      raise ValueError("Email must be a non-empty string.")
    
  @property
  def stylist_id(self):
    return self._stylist_id
  
  @stylist_id.setter
  def stylist_id(self, stylist_id):
    if Stylist.find_by_id(stylist_id):
      self._stylist_id = stylist_id
    else:
      raise ValueError("Stylist ID must reference a stylist in the database.")

  @classmethod
  def create_table(cls):
    """ Create a new table to persist the attributes of Client instances """
    sql = """
      CREATE TABLE IF NOT EXISTS clients (
      id INTEGER PRIMARY KEY,
      name TEXT,
      phone_number TEXT,
      email TEXT,
      stylist_id INTEGER,
      FOREIGN KEY (stylist_id) REFERENCES stylists(id))
    """
    CURSOR.execute(sql)
    CONN.commit()

  @classmethod
  def drop_table(cls):
    """ Drop the table that persists Client instances """
    sql = """
      DROP TABLE IF EXISTS clients;
    """
    CURSOR.execute(sql)
    CONN.commit()

  def save(self):
    """ Insert a new row with the name, phone_number, and email values of the current Client object.
      Update object id attribute using the primary key value of new row.
      Save the object in local dictionary using table row's PK as dictionary key"""
    sql = """
      INSERT INTO clients (name, phone_number, email, stylist_id)
      VALUES (?, ?, ?, ?)
    """

    CURSOR.execute(sql, (self.name, self.phone_number, self.email, self.stylist_id))
    CONN.commit()

    self.id = CURSOR.lastrowid
    type(self).all[self.id] = self

  def update(self):
    """Update the table row corresponding to the current Client instance."""
    sql = """
      UPDATE clients
      SET name = ?, phone_number = ?, email = ?, stylist_id = ?
      WHERE id = ?
    """
    CURSOR.execute(sql, (self.name, self.phone_number, self.email, self.stylist_id, self.id))
    CONN.commit()

  def delete(self):
    """Delete the table row corresponding to the current Client instance,
    delete the dictionary entry, and reassign id attribute"""

    sql = """
      DELETE FROM clients
      WHERE id = ?
    """

    CURSOR.execute(sql, (self.id,))
    CONN.commit()

    del type(self).all[self.id]

    self.id = None

  @classmethod
  def create(cls, name, phone_number, email, stylist_id):
    """ Initialize a new Client instance and save the object to the database """
    client = cls(name, phone_number, email, stylist_id)
    client.save()
    return client

  @classmethod
  def instance_from_db(cls, row):
    """Return a Client object having the attribute values from the table row."""

    client = cls.all.get(row[0])
    if client:
      client.name = row[1]
      client.phone_number = row[2]
      client.email = row[3]
      client.stylist_id = row[4]
    else:
      client = cls(row[1], row[2], row[3], row[4])
      client.id = row[0]
      cls.all[client.id] = client
    return client

  @classmethod
  def get_all(cls):
    """Return a list containing one Client object per table row"""
    sql = """
      SELECT *
      FROM clients
    """

    rows = CURSOR.execute(sql).fetchall()

    return [cls.instance_from_db(row) for row in rows]

  @classmethod
  def find_by_id(cls, id):
    """Return Client object corresponding to the table row matching the specified primary key"""
    sql = """
      SELECT *
      FROM clients
      WHERE id = ?
    """

    row = CURSOR.execute(sql, (id,)).fetchone()
    return cls.instance_from_db(row) if row else None

  @classmethod
  def find_by_name(cls, name):
    """Return Client object corresponding to first table row matching specified name"""
    sql = """
      SELECT *
      FROM clients
      WHERE name is ?
    """

    row = CURSOR.execute(sql, (name,)).fetchone()
    return cls.instance_from_db(row) if row else None