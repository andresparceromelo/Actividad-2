class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
        
    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            print("Depósito exitoso. Nuevo balance:", self.balance)
        else:
            print("La cantidad a depositar debe ser mayor que cero.")
    
    def retirar(self, cantidad):
        if 0 < cantidad <= self.balance:
            self.balance -= cantidad
            print("Retiro exitoso. Nuevo balance:", self.balance)
        else:
            print("Fondos insuficientes o cantidad inválida.")
            
    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print("Cuota de manejo aplicada. Nuevo balance:", self.balance)
        
    def mostrar_detalles(self):
        print("Número de cuenta:", self.numero_cuenta)
        print("Propietarios:", self.propietarios)
        print("Balance:", self.balance)
