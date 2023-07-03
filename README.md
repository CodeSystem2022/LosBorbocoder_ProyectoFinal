# LosBorbocoders_ProyectoFinal 🎓
<h1>Los Borbocoders :copyright:</h1>

![243884073-8bb9f52f-2b75-4abc-8ba5-6fa8173ee153](https://github.com/CodeSystem2022/LosBorbocoders_ProyectoFinal/assets/106932015/e83d8129-c773-4296-bb1b-99eede3b2840)

<h2>Tercer Semestre :computer:</h2>

**_¡¡ORGULLOSAMENTE DESDE LA UTN FRSR AL MUNDO!!_**

![KL4vIdvv_400x400](https://github.com/CodeSystem2022/LosBorbocoders_ProyectoFinal/assets/106932015/bee27b9c-a88d-4646-8e32-f8b4d55876e5)

***
## INTEGRANTES:  
  - `Martin Ojeda`
  - `Paulina Rodriguez`
  - `Emilse Zalazar`
  - `Axel Jocelin Fornerod`
  - `Victor Javier Gomez Allosa`
  - `Kevin Nicolas Lopez Cordoba`
  - `Alessandra Marcano`
  - `Matias Didzius`
  - `Augusto Britos`
***

**_Proyecto integramente en PYTHON_**

![python-powered](https://github.com/CodeSystem2022/LosBorbocoders_ProyectoFinal/assets/106932015/f4e0b3cc-bcca-4579-9ebe-eff87c8b757a)

**_Estructura del código_**
```
src/
├── base_datos/
│   ├── __init__.py
│   └── Conexion.py
│
├── services/
│   ├── __init__.py
│   ├── user_service.py
│   └── transaction_service.py
│   
├── models/
│   ├── __init__.py
│   ├── user.py
│   └── transaction.py
│   
└── main.py
```

<h2>¿En qué consiste nuestro proyecto?</h2>

![mobile-wallet-icon-style-free-vector](https://github.com/CodeSystem2022/LosBorbocoders_ProyectoFinal/assets/106932015/c19605b6-1599-4752-94f6-8b4f0ea494ad)


<h3> VIRTUAL WALLET es una billetera virtual, que puede ser muy util de aplicar para cuando se requiere manejar depositos, utilizando registros de usuarios, autenticación, control de saldos y depositos. </h3>

Para lograr eso, procedimos a realizar los siguientes desarrollos:

<h4>1.Registro de usuarios:</h4>

- Crear una función que solicite al usuario un nombre de usuario o email, telefono y contraseña. 

- Crear un servicio que verifique y almacene esta información en la base

- Crear una tabla para almacenar los usuarios.


<h4>2.Autenticación:</h4> 

- Crear una función que solicite al usuario datos de login.
  
- Además que compruebe si los datos ingresados coinciden con los almacenados en la bas y permita el acceso si la autenticación es exitosa.


<h4>3.Saldo de la cuenta:</h4> 

- Crear una función que recupere y muestre el saldo actual del usuario.

- Crear una tabla para almacenar las cuentas y saldos de cuentas de los usuarios en la base.


<h4>4.Depósito</h4>

- Crear una función que solicite al usuario el monto a depositar y que actualize el saldo en la base sumando el deposito.


<h4>5.Retiro:</h4>

- Crear una función que solicite al usuario el monto a retirar que además verifique si el saldo disponible es suficiente para realizar el retiro. En tal caso que actualize el saldo en la base restando el monto retirado.
