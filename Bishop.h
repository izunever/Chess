#pragma once
#include "BasePiece.h"

class Bishop : public BasePiece {
public:
    Bishop(Color color, Position pos);
    virtual ~Bishop();

    bool isValidMove(Position moveToPosition);
};