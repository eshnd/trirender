import processing.core.PApplet;

public class Trirender extends PApplet {

    public static void main(String[] args) {
        PApplet.main("Trirender");
    }

    public void settings() {
        size(800, 600);
    }

    public void setup() {
        background(255);
        float[] p1 = {200, 100};
        float[] p2 = {300, 400};
        float[] p3 = {100, 400};
        triRender(p1, p2, p3);
    }

    public void draw() {
        noLoop();
    }

    void setPixel(float x, float y) {
        point(x, y);
    }

    float[] lineEQ(float x1, float y1, float x2, float y2) {
        float m = (y2 - y1) / (x2 - x1);
        float b = y2 - m * x2;
        return new float[] {m, b};
    }

    void graphLines(float[] l, float x1, float y1, float x2, float y2) {
        float m = l[0];
        float b = l[1];

        int xmin = Math.round(min(x1, x2));
        int xmax = Math.round(max(x1, x2));

        for (int i = xmin; i <= xmax; i++) {
            float y = m * i + b;
            setPixel(i, y);
        }
    }

    void triRender(float[] p1, float[] p2, float[] p3) {
        float[] l1 = lineEQ(p1[0], p1[1], p2[0], p2[1]);
        float[] l2 = lineEQ(p1[0], p1[1], p3[0], p3[1]);
        float[] l3 = lineEQ(p2[0], p2[1], p3[0], p3[1]);

        graphLines(l1, p1[0], p1[1], p2[0], p2[1]);
        graphLines(l2, p1[0], p1[1], p3[0], p3[1]);
        graphLines(l3, p2[0], p2[1], p3[0], p3[1]);
    }
}
