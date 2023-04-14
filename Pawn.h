#pragma once

#include "BasePiece.h"

class Pawn : public BasePiece {
public:
    Pawn(Color color, Position pos);
    virtual ~Pawn();

    bool isValidMove(Position moveToPosition) override;
private:
    bool doubleStepAvailable;
    bool canBePromoted;
};