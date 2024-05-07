<script setup>
import WelcomeItem from './WelcomeItem.vue'
import DocumentationIcon from './icons/IconDocumentation.vue'
import ToolingIcon from './icons/IconTooling.vue'
import EcosystemIcon from './icons/IconEcosystem.vue'
import CommunityIcon from './icons/IconCommunity.vue'
import SupportIcon from './icons/IconSupport.vue'
</script>

<template>
  <WelcomeItem>
    <template #icon>
      <DocumentationIcon />
    </template>
    <template #heading >
      <a href="../views/TasksView.vue">Tasks</a>
    </template>

    Lobbys main aim is to provide users a solid and simple tasks management system
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <ToolingIcon />
    </template>
    <template #heading><a href="">Version control System</a></template>
    Aim to implement a version control system to keep track of the changes made to the tasks
    using <a href="https://git-scm.com/doc">GIT</a>.
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <EcosystemIcon />
    </template>
    <template #heading><a>Todo</a></template>
    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Praesentium natus nobis
    , fuga velit excepturi pariatur consectetur dolore! Architecto nihil, ipsum autem in cum neque modi asperiores id officiis quae impedit.
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <CommunityIcon />
    </template>
    <template #heading><a>Todo</a></template>
    Lorem ipsum dolor sit, amet consectetur adipisicing elit. Officia cupiditate, laudantium cum ab eligendi 
    çconsectetur porro, hic repellat perspiciatis pariatur earum voluptatem ex doloremque inventore nisi atque fugiat distinctio animi?
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <SupportIcon />
    </template>
    <template #heading><a>Support lobby</a></template>

    As an independent project, Vue relies on community backing for its sustainability. You can help
    us by
    <a href="" target="_blank" rel="noopener">following us</a>.
  </WelcomeItem>
</template>
