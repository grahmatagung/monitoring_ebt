import minimalmodbus
import serial
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import json
import requests
import time
import datetime
import csv

url = "http://10.46.10.128:5000/dummy_komunikasi_data_v2"
headers = {
'Content-Type': 'application/json'
}
try:
    try:
        # """PZEM 017"""
        # mb_address = 1 # Slave ID of sensor
        # mb = minimalmodbus.Instrument('/dev/ttyUSB0',mb_address)	# Make an "instrument" object called mb (port name, slave address (in decimal))

        # mb.serial.baudrate = 9600				# BaudRate
        # mb.serial.bytesize = 8					# Number of data bits to be requested
        # mb.serial.parity = minimalmodbus.serial.PARITY_NONE	# Parity Setting here is NONE but can be ODD or EVEN
        # mb.serial.stopbits = 2					# Number of stop bits
        # mb.serial.timeout  = 3					# Timeout time in seconds
        # mb.mode = minimalmodbus.MODE_RTU				# Mode to be used (RTU or ascii mode)

        # # Good practice to clean up before and after each execution
        # mb.clear_buffers_before_each_transaction = True
        # mb.close_port_after_each_call = True

        """PZEM 004T"""
        serial = serial.Serial(
                                port='/dev/ttyUSB1',
                                baudrate=9600,
                                bytesize=8,
                                parity='N',
                                stopbits=1,
                                xonxoff=0
                                )

        master = modbus_rtu.RtuMaster(serial)
        master.set_timeout(2.0)
        master.set_verbose(True)
    
    except:
        # """PZEM 017"""
        # mb_address = 1 # Slave ID of sensor
        # mb = minimalmodbus.Instrument('/dev/ttyUSB1',mb_address)	# Make an "instrument" object called mb (port name, slave address (in decimal))

        # mb.serial.baudrate = 9600				# BaudRate
        # mb.serial.bytesize = 8					# Number of data bits to be requested
        # mb.serial.parity = minimalmodbus.serial.PARITY_NONE	# Parity Setting here is NONE but can be ODD or EVEN
        # mb.serial.stopbits = 2					# Number of stop bits
        # mb.serial.timeout  = 3					# Timeout time in seconds
        # mb.mode = minimalmodbus.MODE_RTU				# Mode to be used (RTU or ascii mode)

        # # Good practice to clean up before and after each execution
        # mb.clear_buffers_before_each_transaction = True
        # mb.close_port_after_each_call = True

        """PZEM 004T"""
        serial = serial.Serial(
                                port='/dev/ttyUSB0',
                                baudrate=9600,
                                bytesize=8,
                                parity='N',
                                stopbits=1,
                                xonxoff=0
                                )

        master = modbus_rtu.RtuMaster(serial)
        master.set_timeout(2.0)
        master.set_verbose(True) 
except:
    # try:
    #     """PZEM 017"""
    #     mb_address = 1 # Slave ID of sensor
    #     mb = minimalmodbus.Instrument('/dev/ttyUSB0',mb_address)	# Make an "instrument" object called mb (port name, slave address (in decimal))

    #     mb.serial.baudrate = 9600				# BaudRate
    #     mb.serial.bytesize = 8					# Number of data bits to be requested
    #     mb.serial.parity = minimalmodbus.serial.PARITY_NONE	# Parity Setting here is NONE but can be ODD or EVEN
    #     mb.serial.stopbits = 2					# Number of stop bits
    #     mb.serial.timeout  = 3					# Timeout time in seconds
    #     mb.mode = minimalmodbus.MODE_RTU				# Mode to be used (RTU or ascii mode)

    #     # Good practice to clean up before and after each execution
    #     mb.clear_buffers_before_each_transaction = True
    #     mb.close_port_after_each_call = True
    # except:
    #     """PZEM 004T"""
    #     serial = serial.Serial(
    #                             port='/dev/ttyUSB0',
    #                             baudrate=9600,
    #                             bytesize=8,
    #                             parity='N',
    #                             stopbits=1,
    #                             xonxoff=0
    #                             )

    #     master = modbus_rtu.RtuMaster(serial)
    #     master.set_timeout(2.0)
    #     master.set_verbose(True) 
    pass

finally:
    # header_added = False
    # table_header = ['client_id_6', 'send_to_db_at', 'processing_time_6', 'voltage_6', 'current_6', 'power_6', 'energy_6', 'client_id_7', 'data_created_at', 'processing_time_7', 'voltage_7', 'current_7', 'power_7', 'energy_7', 'power_factor'] 
    # with open('logger_surya_v3_new.csv','a', newline='') as f:
    #     writer = csv.writer(f)
    #     if not header_added:
    #         writer.writerow(i for i in table_header)
    #         header_added = True

    while True:
        # try:
            # """pzem 017"""
            # time_awal_6 = time.time()
            # client_id_6 = 6
            # data_1 =mb.read_registers(0, 8, 4) 
            # voltage_6 = data_1[0]/100
            # current_6 = data_1[1]/100
            # power_6 = round(voltage_6*current_6,5)
            # energy_6 = round(power_6*5/60,5)
            # time_akhir_6 = time.time()
            # processing_time_6 = time_akhir_6-time_awal_6

            """pzem 004t"""
            time_awal_7 = time.time()
            client_id_7 = 7
            data_2 = master.execute(1, cst.READ_INPUT_REGISTERS, 0, 10)
            voltage_7 = data_2[0] / 10.0
            current_7 = (data_2[1] + (data_2[2] << 16)) / 1000.0
            power_7 = round(voltage_7*current_7,5)
            energy_7 = round(power_7*5/60,5)
            power_factor = data_2[8]/100.0
            time_akhir_7 = time.time()
            processing_time_7 = time_akhir_7-time_awal_7

            """DATA CREATED AT"""
            data_created_at = datetime.datetime.now()+datetime.timedelta(hours=7)

            # """CSV"""
            # data = [client_id_6, data_created_at, processing_time_6, voltage_6, current_6, power_6, energy_6, client_id_7, data_created_at, processing_time_7, voltage_7, current_7, power_7, energy_7, power_factor]
            # with open('logger_surya_v3_new.csv','a', newline='') as f:
            #     writer = csv.writer(f)
            #     writer.writerow(data)

            """SEND TO SERVER -> DATABASE"""
            # """PZEM 017"""
            # send_to_db_at_6 = datetime.datetime.now()+datetime.timedelta(hours=7)
            # payload_6 = json.dumps(
            #     {'client_id':client_id_6,
            #      'data':
            #     {
            #     'send_to_db_at': str(send_to_db_at_6),
            #     'processing_time': str(processing_time_6),
            #     'voltage': voltage_6,
            #     'current': current_6,
            #     'power': power_6,
            #     'energy': energy_6,
            #     'power_factor' : 0,
            #     }   
            #     }
            # )

            # response_6 = requests.request("POST", url, headers=headers, data=payload_6)

            """PZEM 004T"""
            send_to_db_at_7 = datetime.datetime.now()+datetime.timedelta(hours=7)
            payload_7 = json.dumps(
                {'client_id':client_id_7,
                'data':
                {
                'send_to_db_at': str(send_to_db_at_7),
                'processing_time': str(processing_time_7),
                'voltage': voltage_7,
                'current': current_7,
                'power': power_7,
                'energy': energy_7,
                'power_factor' : power_factor,
                }   
                }
            )

            response_7 = requests.request("POST", url, headers=headers, data=payload_7)

            # print(response_6.text)
            print(response_7.text)

            # print(payload_6)
            # print(payload_7)
            time.sleep(5)
                
        # except:
            # try:
                # try:
                #     """pzem 017"""
                #     time_awal_6 = time.time()
                #     client_id_6 = 6
                #     data_1 =mb.read_registers(0, 8, 4) 
                #     voltage_6 = data_1[0]/100
                #     current_6 = data_1[1]/100
                #     power_6 = round(voltage_6*current_6,5)
                #     energy_6 = round(power_6*5/60,5)

                #     time_akhir_6 = time.time()
                #     processing_time_6 = time_akhir_6-time_awal_6
                    
                #     """DATA CREATED AT"""
                #     data_created_at = datetime.datetime.now()+datetime.timedelta(hours=7)
                         
                #     """CSV"""
                #     data = [client_id_6, data_created_at, processing_time_6, voltage_6, current_6, power_6, energy_6, 7, data_created_at, 0, 0, 0, 0, 0, 0]
                #     with open('logger_surya_v3_new.csv','a', newline='') as f:
                #         writer = csv.writer(f)
                #         writer.writerow(data)

                    # """SEND TO SERVER -> DATABASE"""
                    # send_to_db_at_6 = datetime.datetime.now()+datetime.timedelta(hours=7)
                    # payload_6 = json.dumps(
                    #     {'client_id':client_id_6,
                    #     'data':
                    #     {
                    #     'send_to_db_at': str(send_to_db_at_6),
                    #     'processing_time': str(processing_time_6),
                    #     'voltage': voltage_6,
                    #     'current': current_6,
                    #     'power': power_6,
                    #     'energy': energy_6,
                    #     'power_factor' : 0,
                    #     }   
                    #     }
                    # )
 
                    # response_6 = requests.request("POST", url, headers=headers, data=payload_6)
                    # print(response_6.text)
                    # # print(payload_6)
                    # time.sleep(5)
 
                # except:
                #     """pzem 004t"""
                #     data_2 = master.execute(1, cst.READ_INPUT_REGISTERS, 0, 10)
                #     voltage_7 = data_2[0] / 10.0
                #     current_7 = (data_2[1] + (data_2[2] << 16)) / 1000.0
                #     power_7 = round(voltage_7*current_7,5)
                #     energy_7 = round(power_7*5/60,5)
                #     power_factor = data_2[8]/100.0
 
                #     time_akhir_7 = time.time()
                #     processing_time_7 = time_akhir_7-time_awal_7
 
                #     """DATA CREATED AT"""
                #     data_created_at = datetime.datetime.now()+datetime.timedelta(hours=7)
                         
                #     """CSV"""
                #     data = [6, data_created_at, 0, 0, 0, 0, 0, client_id_7, data_created_at, processing_time_7, voltage_7, current_7, power_7, energy_7, power_factor]
                #     with open('logger_surya_v3_new.csv','a', newline='') as f:
                #         writer = csv.writer(f)
                #         writer.writerow(data)
 
                #     """SEND TO SERVER -> DATABASE"""
                #     send_to_db_at_7 = datetime.datetime.now()+datetime.timedelta(hours=7)
                #     payload_7 = json.dumps(
                #         {'client_id':client_id_7,
                #         'data':
                #         {
                #         'send_to_db_at': str(send_to_db_at_7),
                #         'processing_time': str(processing_time_7),
                #         'voltage': voltage_7,
                #         'current': current_7,
                #         'power': power_7,
                #         'energy': energy_7,
                #         'power_factor' : power_factor,
                #         }   
                #         }
                #     )

                #     response_7 = requests.request("POST", url, headers=headers, data=payload_7)
                #     # print(payload_7)
                #     print(response_7.text)
                #     time.sleep(5)

            # except:
            #     print("pass: error")
            #     pass
