from tests.test_login import test_login_exitoso
from tests.test_checkout import test_checkout_validacion


print("================================")
print("   SUITE SMOKE - SAUCEDEMO")
print("================================")

print("\nEjecutando AUT-01...")
test_login_exitoso()

print("\nEjecutando AUT-02...")
test_checkout_validacion()

print("\n================================")
print("   TODAS LAS PRUEBAS EXITOSAS")
print("================================")