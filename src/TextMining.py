from src.Parser import Parser
import re

class TextMining(Parser):
  pass

  def __init__(self, name):
    self.name = name
    self.text = "Hello world, this is username = @Mike " \
                "also check {price} if username = @Nacy exist in [ this : array ]. " \
                "start day after tomorrow end" \
                "Have a nice day"
    self.rulesBetween = [ "{...}", "[...]", "start...end"]
    self.rulesBetweenResult = []
    self.rulesStart = [{"keyword": "username", "symbol_to": "="}, {"keyword": "this", "symbol_to": ":"}]
    self.rulesStartResult = [ ]

  def hello (self):
    #
    # simulateAI: [{ name: "happy", keywords: [] }] -> number of meets 2 | 3 | 10
    # [{ rule: "=", matchWord: "username" }]
    # return { simulateAI: [{ name:"happy",  }] }
    #
    # 1 --> self.findKeywords(["hello", "nice", "one"], "hello world nice one")

    rules_between = [
      "{...}", "[...]"
    ]

    self.searchBetween()
    self.searchByStart()
    print(self.rulesBetweenResult)
    print(self.rulesStartResult)
    print()



    #print(re.findall(f"(?<=hello) ?{symboll} ?(\S*)", "hello : user%n2am123asde nasidj  asd"))

  def searchBetween (self):
      for x in self.rulesBetween:
        current = self.ruleParseBetween(x, self.text)
        if current != -1:
          self.rulesBetweenResult.append({"rule": x, "found": current})

  def searchByStart (self):
      for x in self.rulesStart:
        self.rulesStartResult.append({
          "rule": x,
          "found": self.ruleParseStartingWith(x["keyword"], x["symbol_to"], self.text)
        })