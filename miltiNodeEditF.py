#Write a GUI tool using PySide to allow you to change a knob value on one or more nodes. The selection type is by class or name of the node. Do your best to make the tool initiative and user-friendly.

#multinodeedit done by OT
import sys
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget

class Panel(QWidget):
   
    def __init__(self):
        super(Panel, self).__init__()
        
        self.initUI()
        
     # MAIN LAYOUT FUNCTION  
    def initUI(self):
        #set the lines
        self.classLine = QLineEdit() 
        self.classLine.setPlaceholderText("Enter name of Node's Class!, ex:Blur")

        self.knobLine = QLineEdit()
        self.knobLine.setPlaceholderText("Enter name of knob wishing to change!")
        self.knobLine.setToolTip("knob name")
        self.knobLine.setDisabled(True)

        self.knobValueLine = QLineEdit()
        self.knobValueLine.setPlaceholderText("Enter a new for knobX!")
        self.knobValueLine.setToolTip("knob value")
        self.knobValueLine.setDisabled(True)

        #set the buttons
    
        self.button1 = QPushButton("Select") #lable of the button
        self.button1.setText("Next") #text to the button
        self.button1.setToolTip("this is a tooltip")
        self.button1.setCheckable(True) #shows the state of the button
        #when button1 clicks:
        #--check if anything is being Entered?
        #--store the value of classLine
        #--check if there is more than 2 node with this className
            #if YES:
                #--disable the button1
                #--disable the classLine
                #--Enable the knobLine
                #--Enable the button2
        self.button1.clicked.connect(self.onClickNext1)
        

        self.button2 = QPushButton("button2")
        self.button2.setText("Next2")
        #push.setIcon(QIcon("Path"))
        #push.setShortcut("a")
        self.button2.setDisabled(True)
        
        #when button2 clicks:
        #--store the value of knobLine
        #A OR B
        #A--check if this knob existed
            #if YES:
                #disable knobLine
                #--disable button2
                #--enable knobValueLine
                #--enable changeKnobButton
        #B
        #self.button2.clicked.connect(self.onClickNext2)
        
      
        self.changeKnobButton = QPushButton("button3")
        self.changeKnobButton.setText("Change knobs")
        self.changeKnobButton.setDisabled(True)

        #ChangeKnob button
        #--check if user filled knob name AND knob value?
        #--store knobLine as self.userKnob
        #--store knobValueLine as userKnobValue 
        #--select all the nodes with self.userClass
           #change all the knobValueLine' values to userKnobValue  
   
    
        self.changeKnobButton.clicked.connect(self.onClickChangeKnob)

        #set the Layout
        layout = QVBoxLayout() 
        layout.addWidget(self.classLine)  #adding the line to the Layout
        layout.addWidget(self.button1)
        layout.addWidget(self.knobLine)
        #layout.addWidget(self.button2)
        layout.addWidget(self.knobValueLine)
        layout.addWidget(self.changeKnobButton)
        
        
        self.setLayout(layout) 

      
    #Once we click this happens            
    def onClickNext1(self):
        self.userClass = self.classLine.text()
        self.checkUserClass()
        #print( self.nodeCounter)     NodeCounter works
        if self.nodeCounter ==0:
            print("there is no node with this Name")
            nuke.message("there is no node with this Name")
        elif self.nodeCounter >=2 :
            self.classLine.setDisabled(True)
            self.button1.setDisabled(True)
            self.knobLine.setDisabled(False)
            #self.button2.setDisabled(False)
            self.knobValueLine.setDisabled(False)
            self.changeKnobButton.setDisabled(False)
        else:
            #print("you dont really need this tool!")
            nuke.message("you dont really need this tool!")
       

    def checkUserClass(self):
        nodes = nuke.allNodes()
        self.nodeCounter = 0
        for node in nodes:
            #print (node.Class())
             #self.line.setText(node.Class()) #why not working
              if node.Class() ==self.userClass:
                  self.nodeCounter = self.nodeCounter + 1
                      
       
       #not being used
    def onClickNext2(self):
        self.userKnob = self.knobLine.text()
        nodes = nuke.allNodes()
        for node in nodes:
            if node.knob.name()== self.userKnob:
                print("YESS")
            else:
                print("there is no knob with this name in this class") 

    def onClickChangeKnob(self):
        self.userKnob = self.knobLine.text()#Knob NAme
        #print(self.userKnob)
        self.userKnobValue =self.knobValueLine.text()#knob Value
        #print(self.userKnobValue)
        nodesX = nuke.allNodes(self.userClass)
        for node in nodesX:
            #if node.knob.name() == self.userKnob:
                node.knob(self.userKnob).setValue(int(self.userKnobValue))
             #node.knob(self.userKnob).setValue(float(self.userKnobValue))
            #else:
                #print("there is no knob with this name")

    #adjust the size of line Box relative to the inputs
    def update(self): 
        self.line.adjustSize()
  
#set the Panel
panel = Panel() 
panel.show()

