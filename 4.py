class Dog(): # Название класса
	def __init__(self, name, age): # Простая модель собаки. Инициализируем атрибуты имя и возраст
		self.name = name
		self.age = age
		print('собака создана')
		self.comand_reading = 0

	def sit(self): # метод, который будет приказывать собаке сесть
		print(self.name.title() + ' сел')

	def jump(self): # метод, который будет приказывать собаке прыгать
		print(self.name.title() + ' сделал прыжок')

	def read_comand (self):
		print ('Наша собака знает: ' + str(self.comand_reading) + ' команд')

	def update_comand(self, com):
		self.comand_reading = com
		if com >= self.comand_reading:
			self.comand_reading = com
		else:
			print('Они не забывают команды!')

	def increment_comand(self, com):
		self.comand_reading += com


my_dog = Dog('Жучка', 4)
print(my_dog.age)
#my_dog_2 = Dog('Тузик', 7)
#print(my_dog_2.name)
my_dog.jump()
#my_dog_2.sit()
my_dog.read_comand()
my_dog.update_comand(3)
my_dog.update_comand(1)
my_dog.read_comand()