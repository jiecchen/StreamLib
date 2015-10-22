#ifndef __COUNT_MIN_H__
#define __COUNT_MIN_H__
#include "config.h"
#include <vector>
#include "Sketch.h"

typedef std::vector<ItemType> Buffer;



/* CountMin_Basic only processes integer stream */
class CountMin_Basic: public Sketch {
private:
  int m; // size of each buffer
  int d; // # of copies of buffer
  std::vector<Buffer> d_buf;
  std::vector<int> seeds;
public:
  CountMin_Basic(int _m, int _d=20);
  void processItem(ItemType item, double weight=1);
  double estTotWeight(ItemType item);
};





#endif

















