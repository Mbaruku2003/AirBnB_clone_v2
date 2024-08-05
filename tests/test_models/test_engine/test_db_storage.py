#!/usr/bin/python3
"""Test file stoage class."""


class TestFileStorage(unittest.TestCase):
    def test_all_returns_as_dict(sel):
        """make sure they are dict."""

        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db' 'not testing db storage')
    def test_all_no_class(self):
        """test that they return rows when no classs is specified."""

        statesdta = {"name": "Nairobi"}
        newstate = State(**statesdta)
        models.storage.new(newstate)
        models.storage.save()

        session = models.storae.DBStorage__session

        allobjects = session.query(State).all()
        self.assertTre(len(allobjects) > 0)

    @unittest.skipIf(models.storage_t != 'db', 'not testing db storage')
    def test_new(self):
        """test that a new object is added to the dtabase."""

        state_data = {"name": "Machakos"}
        new_state = State(**state_data)
        models.storage.new(new_state)
        session = models.storage.DBStorage__session
        
        retreived_state = session.query(State).filter_by(id=new_state).first()
        self.assertEqual(retreived_state.id, new_state.id)
        self.assertEqual(retreived_state.name, new_state.name)
        self.assertIsNone(retreived_state)

    @unittest.skipIf(models.storage_t != 'db', 'not testing db storage')
    def test_save(self):
        """check if objects are stored in json."""

        state_data = {"name": "Cairo"}
        new_state = State(**state_data)
        models.storage.new(new_state)
        models.storage.save()
        session = models.storage.DBStorage__session
        retreived_state = session.query(State).filter_by(id=new_state).first()
    
    @unittest.skipIf(models.storage_t != 'db', 'not testing db storage')
    def test_get(self):
        """Test method fo obtaining an instance db storage."""

        storage = models.storage
        storage.reload()
        state_data = {"name": "brazilia"}
        state_instance = State(**state_data)
        retreived_states = storage.get(State, state_instance.id)
        self.assertEqual(state_instance, retreived_states)
        fake_stateid = storage.ge(State, 'fakes_id')
        self.assertEqual(fake_stateid, None)

    @unittest.skipIf(models.storage_t != "db", "not testing db storage")
    def test_count(self):
        """Counts the number of instances."""

        storage = models.storage
        storage.reload()
        state_data = {"name": "Malawi"}
        state_instance = State(**state_data)
        storage.new(state_instance)
        city_daa = "
