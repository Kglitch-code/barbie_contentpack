from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase): 
	
	def __init__(self):
		ShowBase.__init__(self)
		panel = loader.loadModel("phase_3/models/props/panel.bam")
		panel.reparentTo(render)

app = MyApp()
app.run()
