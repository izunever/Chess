#pragma once
#include "BasePiece.h"

class Queen : public BasePiece {
public:
    Queen(Color color, Position pos);
    virtual ~Queen();

    bool isValidMove(Position moveToPosition);
private:

};