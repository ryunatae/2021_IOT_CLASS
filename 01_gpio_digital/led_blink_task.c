#include <wiringPi.h>
#define LED_PIN 7 
#define YELLOW_PIN 5
#define GREEN_PIN 4

int main (void)
{
    wiringPiSetup () ;
    pinMode (LED_PIN, OUTPUT) ;
    pinMode (YELLOW_PIN, OUTPUT) ;
    pinMode (GREEN_PIN, OUTPUT) ;
    digitalWrite (LED_PIN, HIGH) ;  
    delay (2000) ;
    digitalWrite (LED_PIN, LOW) ;  
    digitalWrite (YELLOW_PIN, HIGH) ;  
    delay (2000) ;
    digitalWrite (YELLOW_PIN, LOW) ;
    digitalWrite (GREEN_PIN, HIGH) ;  
    delay (2000) ;
    digitalWrite (GREEN_PIN, LOW) ;  
    delay (2000) ;
   return 0;
}