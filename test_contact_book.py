from contact_book import create_dictionary,add_contact,display_contact_list
import pytest

def test_create_dictionary():
    #This test help me to prove that my current converted dictionary from csv file has 
    #the same  key value pairs after i add a new contact so in this case I'm testing two functions.

    contact_dic = create_dictionary('contacts.csv')
    new_contact = ['Paul','0969811811','bro']
    add_contact(new_contact)
    doble= contact_dic.copy()
    assert contact_dic == doble
def test_diplay_list():
    #This is an example to test my display function I will do this with an example dictionary
    #to test if the example dictionary is equal to the same dictionary using my display_contact_list function
    dictionary_contact = { 'Mom': ['0980008072','None'],
    'Pau':['0967422278','linarell6@gmail.com'],
    'Dad': ['0969811811','second_a.r@hotmail.com']   
    }
    
    assert display_contact_list(dictionary_contact) == dictionary_contact
        
            
pytest.main(["-v", "--tb=line", "-rN", __file__])

