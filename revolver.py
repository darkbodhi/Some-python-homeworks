class Revolver:

    def __init__(self, name, bullets, actualbullets, readyforfire):
        self.name = name
        self.bullets = int(bullets)
        self.actualbullets = int(0)
        self.readyforfire = bool(False)

    def description(self):
        print("This model is called {}. It has {} bullet slots. Currently it has {} in it. It is {} that it is ready \n"
              "for fire. To shoot it you need to pull on the \n"
              "trigger and charge in the bullets\n".format(self.name, self.bullets, self.actualbullets, self.readyforfire))

    def shoot(self):
        if not self.trigger_check():
            raise Exception("Critical error. The gun was not ready for fire.")
        elif self.actualbullets == 0:
            self.readyforfire = False
            print("click")
        else:
            print("BANG!")
            self.actualbullets -= 1
            self.readyforfire = False

    def charge(self):
        if self.actualbullets < self.bullets:
            self.actualbullets +=1
            print('{} of {} bullet slots is charged.'.format(self.bullets, self.actualbullets))
        else:
            print("The cylinder is already full.")

    def trigger(self):
        if not self.trigger_check():
            self.readyforfire = True

    def trigger_check(self):
        return self.readyforfire


a = Revolver("smithwesson", 6, 0, False)
b = Revolver("brauning", 5, 0, False)

