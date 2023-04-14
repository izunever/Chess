#pragma once

#include "BasePiece.h"

class King : public BasePiece {
public:
    King(Color color, Position pos);
    virtual ~King();

    bool isValidMove(Position moveToPosition);
};
