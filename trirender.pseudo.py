fn triRender(p1:array, p2:array, p3:array, COLOR:string, FILL:bool){

  # all verticies translated to 2D, so each array has a length of y2-y1
  # assuming a setPixel() function preset in the programming language (even 8086 assembly has one)
  # file uses python file extension for correct code coloring in most editors

  xs = (list)[]
  ys = (list)[]

  fn lineEQ(x1, y1, x2, y2){
    m = (y2 - y1) / (x2 - x1)
    b = y2 - m * (x2)

    float[] eq = {m,b}
    return eq
  }

  fn graphLine(l, x1, y1, x2, y2){
    m,b = l[0],l[1]

    xmin = min(x1,x2)
    xmax = max(x1,x2)
    ymin = min(y1,y2)
    ymax = max(y1,y2)
    float[] domain = {xmin,xmax}

    for (i = xmin; i < (xmax+1); i++){
      y = (m*i) + b 
      ys.add(y)
      xs.add(i)  
      setPixel(estimate(i),estimate(y), COLOR)
    }
  }
  fn fill(){
    xs = [x for x in xs if x not in {p1[0], p2[0], p3[0]}]
    ys = [y for y in ys if y not in {p1[1], p2[1], p3[1]}]
    for (int i = 0; i < len(xs); i++){
      xv = xs[i]
      yv1 = ys[i]
      xs.remove(xv)
      ys.remove(yv1)
      xj = 0
      while(xs[xj] != xs[i]){
        xj++ 
      }
      xs.remove(xv[xj])
      yv2 = ys[xj]
      ys.remove(yv[xj])
      ymin = min(yv1, yv2)
      ymax = max(yv1,yv2)
      for(int i = ymin; i < (ymax + 1); i++){
        setPixel(xv,i)
      }
    }
  }

  l1 = (array) lineEQ(p1[0], p1[1], p2[0], p2[1])
  l2 = (array) lineEQ(p1[0], p1[1], p3[0], p3[1])
  l3 = (array) lineEQ(p2[0], p2[1], p3[0], p3[1])

  graphLine(l1, p1[0], p1[1], p2[0], p2[1])
  graphLine(l2, p1[0], p1[1], p3[0], p3[1])
  graphLine(l3, p2[0], p2[1], p3[0], p3[1])
}
