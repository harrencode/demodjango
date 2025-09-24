# Create your tests here.
from django.test import TestCase
from api.models import TodoItem
class TodoItemTestCase(TestCase):

    # creates two TodoItem objects in the test database.
    def setUp(self):
        TodoItem.objects.create(
            title="choose car to buy",
            content="BYD, TOyota, Maruti",
            completed=False)
        TodoItem.objects.create(
            title="30 mins exercise",
            content="Running, pushups, lifting",
            completed=True)
        

        
    # Test the string representation of TodoItem   
    def test_todoitem_str(self):
        item = TodoItem.objects.get(title="choose car to buy")
        self.assertEqual(str(item), "choose car to buy")


    # Test the completed field working or not
    def test_todoitem_completed(self):
        item = TodoItem.objects.get(title="30 mins exercise")
        self.assertTrue(item.completed)



    #test that deleting works
    def test_delete_todoitem(self):
        item = TodoItem.objects.get(title="30 mins exercise")
        item.delete()
        self.assertEqual(TodoItem.objects.filter(title="30 mins exercise").count(), 0)
