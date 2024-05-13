import time as tiempo;

#declaración de variables
sueldo_bruto=0;
nombre="";
desc_afp=0.10;
desc_fonasa=0.07;
horas_extras=0;
bandera_sueldo_nombre=True;
hora_normal=1;
hora_extra=1.5;
horas_mensuales=180;
#ingreso de datos

#ciclos e iteraciones, salida
while bandera_sueldo_nombre:
        
        nombre=input("Ingresa tu nombre: ");
        try:
            sueldo_bruto=int(input("Ingresa tu sueldo bruto: "));
            horas_extras=int(input("Ingresa la cantidad de horas extras trabajadas: "));
        except ValueError:
            print("El valor ingresado no es válido, intentalo nuevamente");
        else:
            
            cant_horas_extras=horas_extras*hora_extra;
            monto_horas_extras=(sueldo_bruto/180)*cant_horas_extras;
            sueldo_bruto_total=monto_horas_extras+sueldo_bruto;
            total_descuentos= sueldo_bruto_total*(desc_afp+desc_fonasa);
            sueldo_liquido=(sueldo_bruto_total-total_descuentos);
            bandera_sueldo_nombre=False;

print(f"Sueldo Bruto: ${sueldo_bruto:,.0f}");
#lo que está después de la variable sirve para separar los números por comas, y decirle 
#al programa que no muestre decimales.
print(f"Horas Extras: {horas_extras:,.1f}");
print(f"Monto Horas Extras: ${monto_horas_extras:,.0f}");
print(f"Sueldo Bruto Total: ${sueldo_bruto_total:,.0f}");
print(f"Descuento AFP (10%): ${sueldo_bruto_total*desc_afp:,.0f}");
print(f"Descuento FONASA (7%): ${sueldo_bruto_total*desc_fonasa:,.0f}");
print(f"Total Descuentos: ${total_descuentos:,.0f}");
print(f"Sueldo Líquido: ${sueldo_liquido:,.0f}");












