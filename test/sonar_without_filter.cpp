#include <NewPing.h>
#include <Arduino.h>

#define TRIGGER_PIN 2
#define ECHO_PIN 3
#define MAX_DISTANCE 200

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // Cria um objeto NewPing para o sensor ultrassônico

void setup() {
  Serial.begin(9600);
}

void loop() {
  unsigned int duration = sonar.ping_median(5); // Realiza a medição da duração do eco em microssegundos
  double distance_cm = (duration / 2.0) * 0.0343; // Converte a duração do eco em centímetros

  // Imprimir a distância sem filtrar para fins de debugging
  Serial.print("Distância sem filtrar: ");
  Serial.print(distance_cm);
  Serial.println(" cm");

  // Aguarde um curto período antes da próxima leitura
  delay(1000); // Espera 1 segundo entre as leituras
}
