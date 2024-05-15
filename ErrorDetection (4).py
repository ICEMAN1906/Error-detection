# Name: Aaronbrown

class ErrorDetection:




    def computeCheckSum(self, message, parity):

        """
        compute checksum of message
        """

        def bit_count(x):
            count = 0
            while x:
                count += x & 1
                x >>= 1

            return count

        # Convert message to list of ASCII
        ASSIIlist=[ord(char) for char in message]

        for i in range(len(ASSIIlist)):
            # Count the number of ones in the binary representation
           ones= bit_count(ASSIIlist[i])
           if ones % 2 !=parity:
               ASSIIlist[i] |=1 <<7 # Set bit to 0

        # Convert the list of integers back to a string of characters

        newmessage = ''.join(chr(char) for char in ASSIIlist)

        return newmessage





    def verifyCheckSum(self, message, parity):
        """
            Verify the checksum of message.


            """
        def bit_count(x):
            count = 0
            while x:
                count += x & 1
                x >>= 1

            return count


        ASSIIlist = [ord(char) for char in message] #make ord able to be applied in a list a
        flag= False
        # Apply parity check and set most-significant bit to 0 if needed
        for i in range(len(ASSIIlist)):
            ones = bit_count(ASSIIlist[i])
            if ones % 2 != parity:
                flag=True
                ASSIIlist[i] &= ~(1 << 7)# Set significant bit to 0

        newmessage = ''.join(chr(char) for char in ASSIIlist) # Convert list of integers back to a string of characters

        return flag,newmessage



