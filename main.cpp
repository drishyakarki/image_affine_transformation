#include "Image.h"

int main(int argc, char** argv) {
    Image test("first_test.jpg");

    IMAGE STORING AND CHANGING THE FORMAT BY COPYING DATA
    test.write("same_img_in_png.png");
    Image copy = test;
    for (int i = 0; i < copy.w*copy.channels; ++i){
        copy.data[i] = 255;
    }

    copy.write("copy.png");
    Image blank(100, 100, 3);
    blank.write("null.jpg");

    Image Grayscale Average AND LUM Function
    Image gray_avg = test;
    gray_avg.grayscale_avg();
    gray_avg.write("gray_avg.png");

    Image gray_lum = test;
    gray_lum.grayscale_avg();
    gray_lum.write("gray_lum.png");

    MODIFYING THE COLOR CHANNELS
    test.colorMask(1, 0, 0);

    test.write("blue.png");
    test.write("red.png");

    test.encodeMessage("Add Image Library for Basic Image Manipulation tranieeship-projects/traniee-on-neural-network!1 · created 1 hour ago by Drishya Karki");
    test.write("SecretMessage.png");

    char buffer[256]= {0};
    size_t len = 0;
    test.decodeMessage(buffer, &len);

    printf("Message: %s (%zu)\n", buffer, len);

    Image test1("first_test.jpg");
    Image test2("second_test.jpg");

    Image diff = test1;
    diff.diffmap(test2);
    diff.write("diff.png");

    return 0;
}