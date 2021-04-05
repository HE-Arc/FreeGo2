<template>

  <v-container fluid>
    <v-row>
      <h3 center>Nos sponsors</h3>
    </v-row>
    <v-row dense>
      <v-col
        v-for="card in cards"
        :key="card.title"
        :cols="card.flex"
      >
        <v-card :href=card.href>
          <v-img
            :src="card.src"
          >
          </v-img>
        </v-card>
      </v-col>
    </v-row>
  </v-container>

</template>

<script>

  export default {
    name: 'Sponsors',
    
    data: () => ({
      cards: [
        { title: 'La Kebaberie', flex: 6, href: 'https://www.kebaberie.ch',
          src: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoCoP0P5jAR32hf3V85NC_YxQXk_Bs0Yxa6g&usqp=CAU'},
        { title: 'Société philanthropique suisse UNION', flex: 6, href: 'https://union.swiss',
          src: 'https://www.journaldujura.ch/sites/journaldujura.ch/files/styles/bt_teaser_medium/hash/48/ad/48ad9cd0c7ff6055ea81c9ac9181794e.jpg?itok=AD4ygNOQ' },
        { title: 'CCAP', flex: 6, href: 'https://www.ccap.ch',
          src: 'https://www.retraitespopulaires.ch/sites/default/files/logos/2017-12/Logo%20CCAP.jpg'},
        { title: 'Loterie Romande', flex: 6, href: 'https://www.entraide.ch/fr/neuchatel/accueil',
          src: 'https://www.entraide.ch/sites/default/themes/entraide/images/entraide-n.png'},
        { title: 'Kiwanis', flex: 6, href: 'https://www.kiwanisne2l.ch',
          src: 'https://seeklogo.com/images/K/kiwanis-logo-37730D461D-seeklogo.com.png' },
        { title: 'FM Stores - Volets', flex: 6, href: 'https://www.fmstores.ch',
          src: 'https://bin.staticlocal.ch/localplace-logo/40/4063a6a7c11fbc57313c76a1a9ab3607577fcac4/Capture%20d%EF%BF%BD%EF%BF%BD%EF%BF%BDe%EF%BF%BD%EF%BF%BDcran%202020-05-12%20a%EF%BF%BD%EF%BF%BD%2010.18.10.png'},
      ],
    }),
  }
</script>

<style scoped>
</style>
