import sys
import subprocess

class DeltaDebugger:
    def __init__(self, input_file, test_script):
        self.input_file = input_file
        self.test_script = test_script
        self.current_input = None

    def test_input(self, input_content):
        with open(self.input_file, 'w') as f:
            f.write(input_content)

        result = subprocess.run(['bash', self.test_script], stdout=subprocess.PIPE)
        return result.returncode == 0

    def run(self):
        with open(self.input_file, 'r') as f:
            self.current_input = f.read()

        n = 2
        while True:
            print(f"preprocessing .. rm {n} idxs: [0]")
            for i in range(n):
                chunk_size = len(self.current_input) // n
                start_idx = i * chunk_size
                end_idx = (i + 1) * chunk_size

                if self.test_input(self.current_input[:start_idx] + self.current_input[end_idx:]):
                    print(f"can delete {n} chunks containing {n} idxs: [{i}]")
                    self.current_input = self.current_input[:start_idx] + self.current_input[end_idx:]

            n *= 2

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python dd.py <input_file> -test <test_script>")
        sys.exit(1)

    input_file = sys.argv[1]
    test_script = sys.argv[3]

    dd = DeltaDebugger(input_file, test_script)
    dd.run()
