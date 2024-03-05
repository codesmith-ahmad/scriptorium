
class Styler:
      @staticmethod      
      def apply(string:str,*styles) -> str:
            print("\n"
                  +"\033[1m"  # ANSI escape for bold style
                  +"\033[3m"  # ANSI escape for italic style
                  +"\033[4m"  # ANSI escape for underline style
                  +"\033[5m"  # ANSI escape for blinking effect
                  +"\033[93m" # ANSI escape for bright yellow
                  +"Code/demo by Ahmad Al-Jabbouri"
                  +"\033[0m"  # This ANSI escape removes all styles
                  +"\n" 
            )