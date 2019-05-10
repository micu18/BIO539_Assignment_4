import unittest
import DM_Assig4
 
    class TestFunc(unittest.TestCase):
        def test_count_kmers(self):
            """ Function to test the accuracy of kmers counting """      
            result1=DM_Assig4.count_kmer_2('ATTTGGATTCCAACT',2)
            self.assertEqual(result1, 11)

        def test_pos_kmers(self):
            """ Function to test the counting of observed and possible kmers  """      
            k=2
            result2=DM_Assig4.build_frame(('ATTTGGATTCCAACT')['Observed_kmers'])
            self.assertEqual(result2, 11)
            
            result3=DM_Assig4.build_frame(('ATTTGGATTCCAACT')['Possible_kmers'])
            self.assertEqual(result3, 14)

        def test_complexity(self):
            """ Function to test the accuracy of computed complexity  """  
            result4=DM_Assig4.compute_complexity(('ATTTGGATTCCAACT')['ratio'])
            self.assertEqual(result4, 0.963302752293578)

            
    if __name__ == '__main__':
    unittest.main()

