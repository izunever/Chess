#pragma once

#include "BasePiece.h"

class Rook : public BasePiece {
public:
    Rook(Color color, Position pos);
    virtual ~Rook();

    bool isValidMove(Position moveToPosition);
};