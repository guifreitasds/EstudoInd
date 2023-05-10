import { StyleSheet, Text, View } from 'react-native';
import {ProfileCard} from '../components/ProfileCard/ProfileCard'

export function CaregiverScreen({route, navigation}) {

  return(
    <View style={styles.container}>
      <ProfileCard/>
      <Text>Details Screen</Text>
    </View>
  );


}

const styles = StyleSheet.create({
    container:{
      flex:1,
      backgroundColor: '#FFC9AB'
    },
})