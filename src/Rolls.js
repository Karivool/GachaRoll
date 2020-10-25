import React, { Component } from 'react';
import rolls from './rollsList.js';

class Rolls extends Component {
  constructor(props) {
    super(props);
    this.state = {
      rollList: [],
      lifeSpent: 0,
      rolls: rolls,
    };
    this.rollOnce = this.rollOnce.bind(this);
  }

  getRandomInt(num) {
    let randomNumber = Math.floor(Math.random() * Math.floor(num))
    return randomNumber + 1;
  }

  rollOnce() {
    const drop = this.getRandomInt(10000);
    let currentList = this.state.rollList;
    let currentRolled = this.state.lifeSpent;
    let resultFound = false;
    let rollsIt = 0;
    let prevNum = 0;
    let currNum = rolls[rollsIt][1];
    while (!resultFound) {
      const prizeList = rolls;
      if(drop > prevNum && drop <= currNum) {
        currentList.unshift(rolls[rollsIt][0]);
        currentRolled += 1;
        resultFound = true;
      } else {
        rollsIt += 1;
        prevNum = currNum;
        currNum = prizeList[rollsIt][1];
      }
    }
    this.setState({
      rollList: currentList,
      lifeSpent: currentRolled
    }, this.updateList(currentList, currentRolled))
  }

  updateList(currentList, currentRolled) {
  }

  render() {
    const rollList = this.state.rollList;
    const lifeSpent = this.state.lifeSpent;
    return (
      <div className="results">
        <div className="fixed-interface">
          <div className="roll-button" onClick={this.rollOnce}>ROLL</div>
          <div className="life-interface">
            <div className="life-spent">
              You have made <b>{lifeSpent}</b> rolls, and thus, used up <b>{lifeSpent}</b> weeks of your life span so far.
            </div>
          </div>
        </div>
        <div className="rolls-interface">
          <div className="rolls-made">
            { rollList.map((option, idx) => {
                return (
                  <div className="roll-result"
                    key={`${idx}-roll-result`}
                  >
                  {rollList[idx]}
                  </div>
                )
            })}
          </div>
        </div>
      </div>
    )
  }
}

export default Rolls;
