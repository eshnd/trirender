#include <GL/glut.h>
#include <array>
#include <algorithm>

using namespace std;

const int w = 600;
const int h = 400;

void setPixel(int x, int y) {
    glBegin(GL_POINTS);
        glVertex2i(x, y);
    glEnd();
}

void triRender(const std::array<float, 2>& p1, const std::array<float, 2>& p2, const std::array<float, 2>& p3) {
    float m1, b1, m2, b2, m3, b3;

    auto lineEQ = [](float x1, float y1, float x2, float y2, float &m, float &b) {
        m = (y2 - y1) / (x2 - x1);
        b = y1 - (m * x1);
    };

    auto graphLine = [&](float m, float b, int x1, int y1, int x2, int y2) {
        int xmin = min(x1, x2);
        int xmax = max(x1, x2);

        for (int x = xmin; x <= xmax; x++) {
            int y = static_cast<int>(m * x + b);
            setPixel(x, y);
        }
    };

    lineEQ(p1[0], p1[1], p2[0], p2[1], m1, b1);
    lineEQ(p1[0], p1[1], p3[0], p3[1], m2, b2);
    lineEQ(p2[0], p2[1], p3[0], p3[1], m3, b3);

    graphLine(m1, b1, static_cast<int>(p1[0]), static_cast<int>(p1[1]), static_cast<int>(p2[0]), static_cast<int>(p2[1]));
    graphLine(m2, b2, static_cast<int>(p1[0]), static_cast<int>(p1[1]), static_cast<int>(p3[0]), static_cast<int>(p3[1]));
    graphLine(m3, b3, static_cast<int>(p2[0]), static_cast<int>(p2[1]), static_cast<int>(p3[0]), static_cast<int>(p3[1]));
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(1.0, 1.0, 1.0);

    std::array<float, 2> p1 = {100.0f, 150.0f};
    std::array<float, 2> p2 = {300.0f, 50.0f};
    std::array<float, 2> p3 = {200.0f, 300.0f};

    triRender(p1, p2, p3);

    glFlush();
}

void init() {
    glClearColor(0.0, 0.0, 0.0, 1.0);
    gluOrtho2D(0.0, w, 0.0, h);
}

int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(w, h);
    glutCreateWindow("trirender");
    init();
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}
