class Lion:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def get_needs(self):
        return 50

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Tiger:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def get_needs(self):
        return 45

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Cheetah:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def get_needs(self):
        return 60

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Keeper:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Caretaker:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Vet:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self._budget = budget
        self._animal_capacity = animal_capacity
        self._workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) >= self._animal_capacity:
            return "Not enough space for animal"
        if self._budget < price:
            return "Not enough budget"
        animal_type = animal.__class__.__name__
        self.animals.append(animal)
        self._budget -= price
        return f"{animal.name} the {animal_type} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) >= self._workers_capacity:
            return "Not enough space for worker"
        worker_type = worker.__class__.__name__
        self.workers.append(worker)
        return f"{worker.name} the {worker_type} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = sum(w.salary for w in self.workers)
        if self._budget >= total_salary:
            self._budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self._budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_needs = sum(a.get_needs() for a in self.animals)
        if self._budget >= total_needs:
            self._budget -= total_needs
            return f"You tended all the animals. They are happy. Budget left: {self._budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self._budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if isinstance(a, Lion)]
        tigers = [a for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [a for a in self.animals if isinstance(a, Cheetah)]
        result = f"You have {len(self.animals)} animals\n"
        if lions:
            result += f"----- {len(lions)} Lions:\n" + "\n".join(repr(l) for l in lions) + "\n"
        if tigers:
            result += f"----- {len(tigers)} Tigers:\n" + "\n".join(repr(t) for t in tigers) + "\n"
        if cheetahs:
            result += f"----- {len(cheetahs)} Cheetahs:\n" + "\n".join(repr(c) for c in cheetahs) + "\n"
        return result

    def workers_status(self):
        keepers = [w for w in self.workers if isinstance(w, Keeper)]
        caretakers = [w for w in self.workers if isinstance(w, Caretaker)]
        vets = [w for w in self.workers if isinstance(w, Vet)]
        result = f"You have {len(self.workers)} workers\n"
        if keepers:
            result += f"----- {len(keepers)} Keepers:\n" + "\n".join(repr(k) for k in keepers) + "\n"
        if caretakers:
            result += f"----- {len(caretakers)} Caretakers:\n" + "\n".join(repr(c) for c in caretakers) + "\n"
        if vets:
            result += f"----- {len(vets)} Vets:\n" + "\n".join(repr(v) for v in vets) + "\n"
        return result
