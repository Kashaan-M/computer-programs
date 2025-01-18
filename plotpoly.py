from numpy.polynomial import Polynomial
import numpy as np
import matplotlib.pyplot as plt


class Start:

	def __init__(self):
		self.greet()
		# attribute initialization
		self.usr_coeffs=""
		self.coeffs=[]
		self.poly=[]
		self.start,self.end,self.step=0,0,0

		self.coeffs= self.ask_coeffs()
		self.poly=self.make_poly()
		self.poly_eq()
		self.ask_domain_start()
		self.ask_domain_end()
		self.ask_domain_stepsize()
		self.plot_graph()
		
	def greet(self):
		print("\n*** Welcome to the Polynomial Plotter.***\n",
		"*** A program which uses Python, Numpy and Matplotlib to plot Polynomials ***\n",
		"*"*30,"\n")

	def ask_coeffs(self):
		self.usr_coeffs= input("Please specify the Polynomial Coefficients as a number sequence separated by commas in the following order:\n\nconstant term, coeff. of 'x' term, coeff. of 'x^2' term, coeff. of 'x^3' term (and so on)\n")
		
		try:	
			self.coeffs= [float(i) for i in self.usr_coeffs.split(",")]
			return self.coeffs
		except ValueError:
			print("Oops. Looks like you made a mistake while entering coefficients of the polynomial.\n Please try again")
			self.ask_coeffs()

		

	def make_poly(self):
		self.poly=Polynomial(self.coeffs)
		return self.poly


	def poly_eq(self):
		print("\nYou have entered the below polynomial equation\n")
		print(self.poly)

	def ask_domain_start(self):
		self.start=input("Please enter start value of 'x' axis. (Make sure it is an integer)\n")
		try:
			self.start= int(self.start)
			return self.start
		except:
			self.ask_domain_start()

		

	def ask_domain_end(self):
		self.end = input("Please enter end value of 'x' axis. (Make sure it is an integer)\n")
		try:
			self.end=int(self.end)
			return self.end
		except:
			self.ask_domain_end()
 

	def ask_domain_stepsize(self):
		self.step = input("Please enter step value of 'x' axis. (Make sure it is an integer)\n")
		try:
			self.step=int(self.step)
			return self.step
		except:
			self.ask_domain_stepsize()


	def plot_graph(self):
		print("And the plot for the polynomial function within the specified domain is as follows\n")
		self.x = np.arange(self.start,self.end,self.step,dtype=int)
		fig,ax = plt.subplots()
		ax.plot(self.x,self.poly(self.x),label=f"y = {self.poly}")
		ax.set_xticks(self.x)
		ax.set_yticks(self.poly(self.x))
		ax.legend()
		ax.grid(True)
		plt.show()


if __name__ == "__main__":
	Start()
