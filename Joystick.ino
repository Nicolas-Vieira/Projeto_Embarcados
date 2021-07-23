int eixo_X = A0;
int eixo_Y = A1;
int botao = 2;
String info = " ";

void setup(){
  pinMode (botao, INPUT_PULLUP); //DEFINE A PORTA COMO ENTRADA
  Serial.begin (9600); //INICIALIZA O MONITOR SERIAL
}
void loop(){
  info = analogRead(eixo_X);
  info += " ";
  info += analogRead(eixo_Y);
  info += " ";
  info += digitalRead(botao);
  Serial.println(info);
  delay(150); 
}
