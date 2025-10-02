class Person:
	def __init__(self, name, age):
		self.__name = name
		self.__age   = age 
	def get_name(self):
		return self.__name
	
	def get_age(self):
		return self.__age
		
person = Person("George", 32) 
print(person.get_name()) 
print(person.get_age())

class EmailValidator:
    def __init__(self, min_length, mails, domains):
   
        self.min_length = min_length
        self.mails = mails
        self.domains = domains
    
    def __validate_name(self, name):
        
        return len(name) >= self.min_length
    
    def __validate_mail(self, mail):
        
        return mail in self.mails
    
    def __validate_domain(self, domain):
        
        return domain in self.domains
    
    def validate(self, email):

        if email.count('@') != 1 or email.count('.') != 1:
            return False
        
        username_domain = email.split('@')
        if len(username_domain) != 2:
            return False

        username = username_domain[0]
        domain_full = username_domain[1]
        
        
        if domain_full.count('.') != 1:
            return False
        
        mail_domain = domain_full.split('.')
        if len(mail_domain) != 2:
            return False
        
        mail = mail_domain[0]
        domain = mail_domain[1]
        

        return (self.__validate_name(username) and
                self.__validate_mail(mail) and
                self.__validate_domain(domain))

validator = EmailValidator(min_length=3, mails=["gmail", "abv"], domains=["com", "net"])

print(validator.validate("peter@gmail.com"))  # True

class Mammal:
    __kingdom = "animals" 
    
    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound
    
    def make_sound(self):
        return f"{self.name} makes {self.sound}"
    
    def get_kingdom(self):
        return self.__kingdom
    
    def info(self):
        return f"{self.name} is of type {self.type}"

lion = Mammal("Leo", "Lion", "roar")
print(lion.make_sound()) 
print(lion.get_kingdom())  
print(lion.info()) 

class Account:
	def __init__(self, id, balance, pin):
		self.__id = id
		self.balance = balance
		self.__pin = pin
		
	def get_id(self, PIN):
		if PIN == self.__pin:
			return self.__id
		else:
			return "wrong pin"
			
	def balance(self):
		return self.balance
		
	def change_pin(self, old_pin, new_pin):
		if old_pin == self.__pin:
			self.__pin = new_pin
			return "pin changed"
		else:
			return "wrong pin"
			
account = Account(8827312, 100, 3421) 
print(account.get_id(1111)) 
print(account.get_id(3421)) 
print(account.balance) 
print(account.change_pin(2212, 4321)) 
print(account.change_pin(3421, 1234)) 

input()