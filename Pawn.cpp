#include "Pawn.h"
#include "Board.h"
#include <iostream>

using namespace std;

extern Board chessBoard;

Pawn::Pawn(Color color, Position pos) {
    if(color == Color::Black) {
        this->type = "p";
    }
    else {
        this->type = "P";
    }
    this->color=color;
    this->pos = pos;
    this->doubleStepAvailable = true;
    this->canBePromoted = false;
}

Pawn::~Pawn() {

}

bool Pawn::isValidMove(Position moveToPos) {
    bool isValidMove = false;
    int possibleMove1 = 1;
    int possibleMove2 = 2;

    if (color == Color::Black) {
        possibleMove1 = -1;
        possibleMove2 = -2;
    }

    if (moveToPos.rank == pos.rank + possibleMove1 && moveToPos.file == pos.file && chessBoard.getPiece(moveToPos) == NULL) {
        isValidMove = true;
        doubleStepAvailable = false;
    }

    else if (doubleStepAvailable == true && moveToPos.rank == (pos.rank + possibleMove2) && moveToPos.file == pos.file && chessBoard.getPiece(moveToPos) == NULL) {
        isValidMove = true;
    }

    else if (moveToPos.rank == pos.rank + possibleMove1 && (moveToPos.file == pos.file - 1 || moveToPos.file == pos.file + 1) ) {
        if (chessBoard.getPiece(moveToPos) != NULL && (chessBoard.getPiece(moveToPos)->getColor() != this->color) )  {
            isValidMove = true;
        }
    }
    return isValidMove;
}