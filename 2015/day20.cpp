#include <iostream>

int main(int argc, char **argv)
{
    int house = 826560;
    int highest = 0;

    while (true) {
        house += 1;
        int count = 0;

        for (int i = 1 ; i <= (int)(house / 2)+1 ; i++) {
            if (house % i == 0 && i*50 >= house) {
                count += i*11;
            }
        }
        count += house * 10;

        if (count > highest) {
            std::cout << house << " " << count << std::endl;
            highest = count;
        }

        if (count > 34000000) {
            std::cout << house << std::endl;
            return 0;
        }
    }
}
