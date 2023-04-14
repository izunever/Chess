#pragma once

#include "BasePiece.h"

class Knight : public BasePiece {
public:
    Knight(Color color, Position pos);
    virtual ~Knight();

    bool isValidMove(Position moveToPosition);
};