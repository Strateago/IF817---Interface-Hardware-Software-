#include <stdio.h>

extern float V_cone(float raio, float altura);

int main() {

    float altura = 5.0;

    float raio = 3.0;

    float ret = V_cone(raio, altura);

    printf("Volume do cone eh igual a : %.2f \n", ret);

    return 0;

}

