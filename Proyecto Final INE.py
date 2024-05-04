### INTEGRALES NO ELEMENTALES ###

import math
import numpy as np

class Integrales_No_elementales:

  def __init__(self):
    pass

  def Eliptica(self):#a√(1-k(x^4))
    if ((self.Li**4) > (1/self.k) or (self.Ls**4) > (1/self.k)):
      return "No Dom."
    return self.a*np.sqrt(1-(self.k*((self.x)**4)))

  def Logaritmica(self):
    if (self.k*self.Li) < 0 or (self.k*self.Ls) < 0:
      return "No Dom."
    return self.a/(math.log(self.k*self.x))

  def Gaussiana(self):
    return self.a*math.exp(-self.k*(self.x**2))

  def Dirichlet(self):
    return self.a*math.sin(self.k*self.x)/self.x

  def Fresnel_sen(self):
    return self.a*math.sin(self.k*(self.x**2))

  def Fresnel_cos(self):
    return self.a*math.cos(self.k*(self.x**2))

  def Seleccion(self):
    self.Li = 0.1
    self.Ls = 0.2
    self.a = 1
    self.k = 1
    self.x = self.Li
    self.Funciones = {"E": self.Eliptica, "L": self.Logaritmica, "G": self.Gaussiana, "D": self.Dirichlet, "S": self.Fresnel_sen, "C": self.Fresnel_cos}
    self.Errores = {"E": "La integral no tiene solución en los reales. Tome 'Ls', 'Li' y 'k' tales que Ls^4<=1/k y Li^4<=1/k.",
                    "L": "La integral no tiene solución en los reales. Tome 'Ls', 'Li' y 'k' tales que k*Ls>0 y k*Li>0"}
    self.Forma_Funciones = {"E": "a√(1-k(x^4))", "L": "a/ln(kx)", "G": "a*e^(-k(x^2))", "D": "a*sin(kx)/x", "S": "a*sin(k*(x^2))", "C": "a*cos(k*(x^2))"}
    #BUCLE DE SELECCIÓN
    while True:
      self.Funcion_elegida = input("""Elija la integral no-elemental a calcular escribiendo su respectiva letra entre paréntesis: \n
Elíptica(E), Logarítmica(L), Gaussiana(G), Dirichlet(D), Fresnel Seno(S), Fresnel Coseno(C)\n Función: """)
      if self.Funcion_elegida in self.Funciones:
        print("Función elegida:", self.Funcion_elegida, ". Forma: ", self.Forma_Funciones.get("{}".format(self.Funcion_elegida)))
        break
      else:
        print("No se encontró la función. Escriba una de las letras entre paréntesis en mayúscula.")
    self.Li = float(input("Límite inferior (Li):"))
    self.Ls = float(input("Límite superior (Ls):"))
    self.a = float(input("a = "))
    self.k = float(input("k = "))
    self.n = int(input("Número de intervalos (n):"))
    self.Dx = abs(self.Ls-self.Li)/self.n
    self.Fx_i = list(np.zeros(self.n+1))
    print(self.Fx_i) ##### ##### #####
    self.x_i = list(np.zeros(self.n+1))
    print(self.x_i) ##### ##### #####
    print("self.Ls = ", self.Ls) ##### ##### #####
    print("self.Li = ", self.Li) ##### ##### #####
    print("self.k = ", self.k) ##### ##### #####

  def Integrar_Tc(self):
    self.Seleccion()
    #BUCLE DE INTEGRACIÓN:
    Integral =  0
    i = 0 #Contador e índice
    while i <= self.n:
      # Si los límites están invertidos:
      if self.Li < self.Ls:
        self.x_i[i] = self.Li + i*self.Dx
      elif self.Li > self.Ls:
        self.x_i[i] = self.Li - i*self.Dx
      # Para Discontinuidades (Solo aplica para Dirichlet y Logarítmica)
      if self.x_i[i] == 0:
        if self.Funcion_elegida == "D":
          self.x_i[i]+=0.0001
        if self.Funcion_elegida == "L":
          Integral = "Diverge: Discontinuidad tipo infinito en x = 0"
          break
      if self.Funcion_elegida == "L" and self.x_i[i]*self.k == 1:
        Integral = "Diverge: Discontinuidad tipo infinito en x = {}".format(self.x_i[i])
        break

      self.x = self.x_i[i]
      print("self.x=", self.x) ##### ##### #####
      self.Fx_i[i] = self.Funciones.get("{}".format(self.Funcion_elegida))()
      print("f(x_i)=", self.Fx_i[i]) ##### ##### #####

      #Para valores por fuera del dominio (Solo aplica para Elíptica y Logarítmica)
      if self.Fx_i[i] == "No Dom.":
        print("False") ##### ##### #####
        Integral = self.Errores.get("{}".format(self.Funcion_elegida))
        break
      if i == 0 or i == self.n:
        Integral += (self.Dx*self.Fx_i[i])/2
      else:
        Integral += self.Dx*self.Fx_i[i]
      i+=1
      print("Integral=", Integral)
    # Si los límites están invertidos, la integral es el negativo del resultado
    if type(Integral) != str and self.Ls < self.Li:
      Integral = (-1)*Integral
    print("Integral=", Integral)

INE = Integrales_No_elementales()
I = INE.Integrar_Tc()
