# Electrical and Software

## Flow control

### Hot-fire sequence design

The team is required to stay in the bunker during a hot fire, so the engine must be controlled remotely. We chose to use two ESP32s, **one of which would send commands (**[**`COM Board`**](electrical-and-software.md#com-board)**)**, and **the other would report data (`DAQ Board`)**. Both devices were constructed as state machines, with COM Board connected to the computer to transmit the data reported by the DAQ Board.

Here is a state machine diagram to visualize the communication:&#x20;

<figure><img src="../../.gitbook/assets/ELLIE STATE MACHINE.png" alt=""><figcaption><p>Drawing of the state machine that determined the sequence in which events happened. </p></figcaption></figure>

<details>

<summary>Explanation of the State Machine</summary>

After the initial start-up, the COM board first goes into state 0, then settles in state 1. It instructs the DAQ board to enter state 1 and only poll for data at a relatively slow rate (about 1 data point per second). The COM Board and DAQ board lights would flash when a data packet is successfully sent or received.&#x20;

When button 1 is pressed, the COM board enters state 3, the armed state. The DAQ board receives the command to change state and moves to state 3 as well. Both the COM and DAQ lights become solid to indicate the state change. Here the poling occurs more frequently, and the system is ready to execute the hot-fire stages.&#x20;

After button 2 is pressed, ignition occurs. However, no further actions are happening as a visual confirmation of a visible flame is necessary to continue.&#x20;

Once a visible flame is confirmed, and button 3 is pressed, the COM board enters state 5. The DAQ board, after moving to the same state, enters an automatic process. At this point, instead of commanding, the COM board listens for the status update from the DAQ board.

The DAQ board, at state 5, opens GOX valve and keep the ETH valve closed. After approximately 0.5 second, the board moves to state 6, where both valves are opened. State 7 comes x seconds afterward, x being the planned hot-fire time, and closes the GOX valve. It lasts for another 0.5 second, and transitions into state 8, where both valves are closed. At this point, DAQ resets the state to 0, and pass it back to the COM board, which adjusts the state accordingly. A full hot-fire sequence is complete.&#x20;

Devices connected to DAQ: 4 PTs (pressure transducers), 1 FM (flow meter), load cells.

</details>

### Code Implementation

{% tabs %}
{% tab title="COM Board" %}

{% endtab %}

{% tab title="DAQ Board" %}
{% embed url="https://github.com/calstar/ellie-ground/blob/main/Aurduino/Dev/COMBoard/COMBoard.ino" %}

#### Code Highlights

Since the bunkers and the launch pad are approximately 100 ft apart, using a wired cable between the ESP32s, although reliable and still popular in collegiate teams, was not economically efficient. Instead, we established a wireless connection between the COM and DAQ boards, with an information queue that can hold data while transmitting.

```arduino
//Define communication structure

typedef struct struct_message {
    int messageTime;
     int pt1;
     int pt2;
     int pt3;
     int pt4;
     int lc1;
     int lc2;
     int lc3;
     int fm;
    unsigned char S1;
    unsigned char S2;
        int commandedState = 0;
        int DAQstate=0;

    unsigned char I;
    short int queueSize;
    int Debug;
} struct_message
```

The "pts" are the pressure transducers we implemented throughout the engine system, while the "lcs" are load cells for measuring the engine thrust, and fm is the flow meter measurement. For both sending and receiving data, functions and interrupts are set up to handle.&#x20;

Establishing the data structure for communications:

```arduino
// Create a struct_message called Readings to recieve sensor readings remotely
struct_message incomingReadings;

// in void setup() we register the for a callback function that will be called when data is received
esp_now_register_recv_cb(OnDataRecv);

void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
 // Serial.print("\r\nLast Packet Send Status:\t");
 // Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Delivery Success" : "Delivery Fail");

  if (status == 0){
    success = "Delivery Success :)";
    digitalWrite(INDICATOR2, HIGH);
    receiveTimeDAQ = millis();
  }
  else{
    success = "Delivery Fail :(";
    digitalWrite(INDICATOR2, LOW);
  }

}

// interrupt function, triggered when 
void OnDataRecv(const uint8_t * mac, const uint8_t *incomingData, int len) {
  memcpy(&incomingReadings, incomingData, sizeof(incomingReadings));
  incomingPT1 = incomingReadings.pt1;

     digitalWrite(INDICATOR1,HIGH);

// loading the remote data into local variables
  incomingMessageTime= incomingReadings.messageTime;
  incomingPT2 = incomingReadings.pt2;
  incomingPT3 = incomingReadings.pt3;
  incomingPT4 = incomingReadings.pt4;
  incomingFM = incomingReadings.fm;
  incomingLC1 = incomingReadings.lc1;
  incomingLC2 = incomingReadings.lc2;
  incomingLC3 = incomingReadings.lc3;
  incomingS1 = incomingReadings.S1;
  incomingS2 = incomingReadings.S2;
  queueSize= incomingReadings.queueSize;
  incomingI = incomingReadings.I;
  actualState = incomingReadings.DAQstate;
  incomingDebug= incomingReadings.Debug;

// Rest of code omitted
}
```

In `setup()`, we need to call the following commands to get everything working:

```arduino
//initialize ESP32
   if (esp_now_init() != ESP_OK) {
  //  Serial.println("Error initializing ESP-NOW");
    return;
  }
   // Once ESPNow is successfully Init, we will register for Send CB to
  // get the status of Trasnmitted packet
  esp_now_register_send_cb(OnDataSent);

  // Register peer/ second ESP 32
  memcpy(peerInfo.peer_addr, broadcastAddress, 6);
  peerInfo.channel = 0;
  peerInfo.encrypt = false;

  // Add peer
  if (esp_now_add_peer(&peerInfo) != ESP_OK){
 //   Serial.println("Failed to add peer");
    return;
  }
  // Register for a callback function that will be called when data is received
  esp_now_register_recv_cb(OnDataRecv);
```

The following code is the implementation of the state machine. State cases such as -1, 30, etc. are omited since they are only for testing and debugging purposes. Those states are not a part of the main hot-fire sequence.

```arduino
//State Machine Implementation
case (0): //Default/idle
      idle();
      state=1;  
    break;

  case (1): //Polling
    polling();

    if ((digitalRead(BUTTON2)==1)||(serialState==2)) { state=3; S1=servo1ClosedPosition; S2=servo2ClosedPosition; SendDelay=pollingSendDelay; }
    if (serialState==18) {state=18;} 
    if (serialState==17) {state=17;} 
    if (digitalRead(PRESS_BUTTON)==30) {state=30;}

    break;

  case (2): //Manual Servo Control

 manualControl();
  if ((serialState==40)) { state=0; SendDelay=pollingSendDelay; }

  break;

  case (3): //Armed
    armed();

    //button to ignition 
    if ((digitalRead(BUTTON3)==1)||(serialState==3)) { state=4; S1=servo1ClosedPosition; S2=servo2ClosedPosition; SendDelay=ignitionSendDelay; }
    //RETURN BUTTON
    if ((digitalRead(BUTTON1)==1)||(serialState==1)) { state=1; S1=servo1ClosedPosition; S2=servo2ClosedPosition; SendDelay=pollingSendDelay; }
      
    break;


  case (4): //Ignition

    ignition();
    //HOTFIRE BUTTON
      if ((digitalRead(BUTTON4)==1)||(serialState==4)) state=5; 
      //RETURN BUTTON
      if ((digitalRead(BUTTON1)==1)||(serialState==1)) { state=1; S1=servo1ClosedPosition; S2=servo2ClosedPosition; SendDelay=pollingSendDelay; }
      
    break;
  case (5): //Hotfire stage 1

    hotfire();

    if (actualState==0) state=0;
```
{% endtab %}
{% endtabs %}

### Data acquisition and processing

### Automation in calibration
