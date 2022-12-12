# import kivy module 
import kivy 
    
# this restrict the kivy version i.e 
# below this kivy version you cannot 
# use the app or software 
kivy.require("1.9.1") 
    
# base Class of your App inherits from the App class. 
# app:always refers to the instance of your application 
from kivy.app import App 
    
# creates the button in kivy 
# if not imported shows the error 
from kivy.uix.button import Button 
  
# This layout allows you to set relative coordinates for children. 
from kivy.uix.relativelayout import RelativeLayout 

global show
show = True
class FirstButtonApp(App):

    def build(self):
        global show
 
        # create a fully styled functional button
        # Adding images normal.png and down.png
        btn = Button(text ="Push Me !",
                     background_normal = 'gamesclick.png',
                     background_down = 'gamesclick.png',
                     size_hint = (.3, .3),
                     pos_hint = {"x":0.35, "y":0.3}
                     
                   )
   
        # bind() use to bind the button to function callback
        btn.bind(on_press = self.callback)
        return btn
   
    # callback function tells when button pressed
    def callback(self, event):
        global show
        show = False
        print("button pressed")
        print('Yoooo !!!!!!!!!!!')
 
 
if __name__ == "__main__":
   FirstButtonApp().run()