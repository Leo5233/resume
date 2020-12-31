# -*- coding: utf-8 -*-
import unittest

class test_reverse(unittest.TestCase):
    
    
    def setUp(self):
        self.input_value = {
                              'hired': {
                                'be': {
                                  'to': {
                                    'deserve': 'I'
                                  }
                                }
                              }
                            }
        self.middle = ['hired', 'be', 'to', 'deserve', 'I']
        self.output_value = {
                              'I': {
                                'deserve': {
                                  'to': {
                                     'be': 'hired'
                                  }
                                }
                              }
                            }
    
    def test1(self):
        middle = self.apart(self.input_value)
        self.assertEqual(middle, self.middle)
    
    def test2(self):
        output_ = self.reverse(self.middle)
        self.assertEqual(output_, self.output_value)
    
    def apart(self, input_, words=[]):
        key = list(input_)[0]
        words.append(key)
        if isinstance(input_[key], dict):
            return self.apart(input_[key],words)
        else:
            words.append(input_[key])
            return words
    
    def reverse(self, words):
        key = words.pop(-1)
        if len(words) > 1:
            return {key:self.reverse(words)}
        else:
            return {key: words.pop(-1)}

    def tearDown(self):
        self.input_value = None

if __name__ == '__main__':
    unittest.main()