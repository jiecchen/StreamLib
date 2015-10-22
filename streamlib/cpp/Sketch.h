#ifndef __SKETCH_H__
#define __SKETCH_H__
#include "config.h"


class Sketch {
public:
  virtual void processItem(ItemType item, double weight) = 0;
};

#endif
