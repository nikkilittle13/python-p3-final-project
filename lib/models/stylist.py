# lib/models/stylist.py
from models.__init__ import CURSOR, CONN

class Stylist:

   all = {}

   def __init__(self, name, specialization, years_worked, id=None):
      self.id = id
      self.name = name
      self.specialization = specialization
      self.years_worked = years_worked

   def __repr__(self):
      return f"ID: {self.id} - {self.name}, {self.specialization}, {self.years_worked} years."
   
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
   def specialization(self):
      return self._specialization

   @specialization.setter
   def specialization(self, specialization):
      if isinstance(specialization, str) and len(specialization):
         self._specialization = specialization
      else:
         raise ValueError("Specialization must be a non-empty string.")

   @property
   def years_worked(self):
      return self._years_worked
   
   @years_worked.setter
   def years_worked(self, years_worked):
      if int(years_worked):
         self._years_worked = years_worked
      else:
         raise ValueError("Years worked must be an integer.")

   @classmethod
   def create_table(cls):
      """ Create a new table to persist the attributes of Stylist instances """
      sql = """
         CREATE TABLE IF NOT EXISTS stylists (
         id INTEGER PRIMARY KEY,
         name TEXT,
         specialization TEXT,
         years_worked INTEGER) 
      """
      CURSOR.execute(sql)
      CONN.commit()

   @classmethod
   def drop_table(cls):
      """ Drop the table that persists Stylist instances """
      sql = """
         DROP TABLE IF EXISTS stylists;
      """
      CURSOR.execute(sql)
      CONN.commit()

   def save(self):
      """ Insert a new row with the name, specialization, and years worked values of the current Stylist instance.
      Update object id attribute using the primary key value of new row.
      Save the object in local dictionary using table row's PK as dictionary key"""
      sql = """
            INSERT INTO stylists (name, specialization, years_worked)
            VALUES (?, ?, ?)
      """

      CURSOR.execute(sql, (self.name, self.specialization, self.years_worked))
      CONN.commit()

      self.id = CURSOR.lastrowid
      type(self).all[self.id] = self

   @classmethod
   def create(cls, name, specialization, years_worked):
      """ Initialize a new Stylist instance and save the object to the database """
      stylist = cls(name, specialization, years_worked)
      stylist.save()
      return stylist

   def update(self):
      """Update the table row corresponding to the current Stylist instance."""
      sql = """
         UPDATE stylists
         SET name = ?, specialization = ?, years_worked = ?
         WHERE id = ?
      """
      CURSOR.execute(sql, (self.name, self.specialization, self.years_worked, self.id))
      CONN.commit()

   def delete(self):
      """Delete the table row corresponding to the current Stylist instance,
      delete the dictionary entry, and reassign id attribute"""

      sql = """
         DELETE FROM stylists
         WHERE id = ?
        """

      CURSOR.execute(sql, (self.id,))
      CONN.commit()

      del type(self).all[self.id]

      self.id = None

   @classmethod
   def instance_from_db(cls, row):
      """Return a Stylist object having the attribute values from the table row."""

      stylist = cls.all.get(row[0])
      if stylist:
         stylist.name = row[1]
         stylist.specialization = row[2]
         stylist.years_worked = row[3]
      else:
         stylist = cls(row[1], row[2], row[3])
         stylist.id = row[0]
         cls.all[stylist.id] = stylist
      return stylist

   @classmethod
   def get_all(cls):
      """Return a list containing a Sylist object per row in the table"""
      sql = """
         SELECT *
         FROM stylists
      """

      rows = CURSOR.execute(sql).fetchall()

      return [cls.instance_from_db(row) for row in rows]

   @classmethod
   def find_by_id(cls, id):
      """Return a Stylist object corresponding to the table row matching the specified primary key"""
      sql = """
         SELECT *
         FROM stylists
         WHERE id = ?
      """

      row = CURSOR.execute(sql, (id,)).fetchone()
      return cls.instance_from_db(row) if row else None

   @classmethod
   def find_by_name(cls, name):
      """Return a Stylist object corresponding to first table row matching specified name"""
      sql = """
         SELECT *
         FROM stylists
         WHERE name is ?
      """

      row = CURSOR.execute(sql, (name,)).fetchone()
      return cls.instance_from_db(row) if row else None

   def get_clients(self):
      """Return list of clients associated with current stylist"""
      from models.client import Client
      sql = """
         SELECT * FROM clients
         WHERE stylist_id = ?
      """
      CURSOR.execute(sql, (self.id,),)

      rows = CURSOR.fetchall()
      return [Client.instance_from_db(row) for row in rows]